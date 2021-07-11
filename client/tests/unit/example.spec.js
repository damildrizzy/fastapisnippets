import { shallowMount } from "@vue/test-utils";
import SnippetList from "@/components/SnippetList.vue";

describe("SnippetList.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(SnippetList, {
      props: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
